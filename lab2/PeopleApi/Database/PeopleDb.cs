using Microsoft.EntityFrameworkCore;
using PeopleApi.Database.Entities;

namespace PeopleApi.Database
{
    
    public class PeopleDb : DbContext
    {
        public PeopleDb(DbContextOptions options) : base(options)
        {
        }

        public DbSet<PersonEntity> People { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            var personEntity = modelBuilder.Entity<PersonEntity>();
            personEntity.ToTable("Person");
            personEntity.Property(p => p.FirstName).IsRequired().HasMaxLength(250);
            personEntity.Property(p => p.LastName).IsRequired().HasMaxLength(250);
            personEntity.Property(p => p.PhoneNumber).IsRequired(false).HasMaxLength(12);
        }
    }

}